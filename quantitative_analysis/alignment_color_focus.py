import nest_asyncio
from playwright.sync_api import sync_playwright
nest_asyncio.apply()

def main_sync_jupyter():
    import numpy as np
    import pandas as pd
    from pathlib import Path
    from itertools import combinations
    from colorspacious import cspace_convert
    from scipy.spatial.distance import euclidean
    from tqdm.notebook import tqdm

    ROOT = Path("../generated_guis")
    PROMPTS = ["instruction", "pd_zs", "pd_fs", "ref_instruction"]
    VIEWPORT = {"width": 1280, "height": 800}
    OUT_CSV = "alignment_color_focus.csv"

    def parse_rgb(css_color):
        if not css_color or 'transparent' in css_color:
            return None
        try:
            nums = css_color.replace('rgba(','').replace('rgb(','').replace(')','').split(',')
            nums = [int(float(x.strip())) for x in nums[:3]]
            return np.array(nums, dtype=np.uint8)
        except:
            return None

    def spacing_score_md(boxes):
        if len(boxes) < 2:
            return np.nan
        ys_sorted = np.sort([b['top'] for b in boxes])
        diffs = np.diff(ys_sorted)
        compliant = sum(1 for d in diffs if d % 8 == 0)
        return float(compliant / len(diffs))

    def overlap_md(boxes):
        def safe_z(b):
            z = b.get('z', 0)
            try:
                return int(z)
            except (ValueError, TypeError):
                return 0

        same_plane = [b for b in boxes if safe_z(b) == 0]

        overlaps = 0
        for a, b in combinations(same_plane, 2):
            ax1, ay1, ax2, ay2 = a["left"], a["top"], a["left"]+a["width"], a["top"]+a["height"]
            bx1, by1, bx2, by2 = b["left"], b["top"], b["left"]+b["width"], b["top"]+b["height"]
            inter_w = max(0, min(ax2, bx2) - max(ax1, bx1))
            inter_h = max(0, min(ay2, by2) - max(ay1, by1))
            overlaps += inter_w * inter_h

        canvas_area = VIEWPORT['width'] * VIEWPORT['height']
        return 1 - min(overlaps / canvas_area, 1.0)


    def color_contrast_score(boxes):
        rgbs = [parse_rgb(b.get("bg")) for b in boxes if parse_rgb(b.get("bg")) is not None]
        if len(rgbs) < 2:
            return np.nan
        rgbs = np.array(rgbs)/255.0
        labs = cspace_convert(rgbs, "sRGB1", "CIELab")
        primary_idx = np.argmax([b.get("width",0)*b.get("height",0) for b in boxes])
        primary_lab = labs[primary_idx]
        other_labs = np.delete(labs, primary_idx, axis=0)
        dists = [euclidean(primary_lab, o) for o in other_labs]
        return float(np.clip(np.mean(dists) / 100.0, 0, 1))

    def get_boxes(page):
        return page.evaluate("""
            () => Array.from(document.querySelectorAll('*'))
                .filter(e => {
                    const r = e.getBoundingClientRect();
                    return r.width>0 && r.height>0 &&
                           getComputedStyle(e).visibility !== 'hidden' &&
                           getComputedStyle(e).display !== 'none';
                })
                .map(e => {
                    const r = e.getBoundingClientRect();
                    const cs = getComputedStyle(e);
                    return {
                        left: Math.round(r.left),
                        top: Math.round(r.top),
                        width: Math.round(r.width),
                        height: Math.round(r.height),
                        bg: cs.backgroundColor,
                        z: (cs.zIndex || '0')
                    };
                })
        """)

    def focus_accessibility_metrics_split(page):
        res = page.evaluate("""
        () => {
            const buttons = Array.from(document.querySelectorAll('button, [role=button]'));
            const total = buttons.length;
            const focusable = buttons.filter(b => b.tabIndex >= 0).length;
            const labelled = buttons.filter(b => b.getAttribute('aria-label') || b.getAttribute('contentDescription')).length;
            return {total, focusable, labelled};
        }
        """)
        if res['total']==0:
            return {"focusable_ratio": np.nan, "labelled_ratio": np.nan}
        return {
            "focusable_ratio": float(res['focusable']/res['total']),
            "labelled_ratio": float(res['labelled']/res['total'])
        }

    rows = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport=VIEWPORT)
        page = context.new_page()

        appdirs = [d for d in ROOT.iterdir() if d.is_dir()]
        for appdir in tqdm(appdirs, desc="Evaluating GUIs (Sync, nest_asyncio)"):
            for prompt in PROMPTS:
                html_path = appdir / f"{prompt}.html"
                if not html_path.exists(): continue
                page.goto("file:///" + str(html_path.resolve()))
                page.wait_for_load_state("load")

                boxes = get_boxes(page)
                spacing = spacing_score_md(boxes)
                overlap = overlap_md(boxes)
                color = color_contrast_score(boxes)
                focus = focus_accessibility_metrics_split(page)

                rows.append({
                    "app_id": appdir.name,
                    "prompt": prompt,
                    "n_elements": len(boxes),
                    "spacing_md": spacing,
                    "overlap_md": overlap,
                    "color_contrast": color,
                    **focus
                })

        browser.close()

    df = pd.DataFrame(rows)
    df.to_csv(OUT_CSV, index=False)
    print(f"✅ Rezultati shranjeni v: {OUT_CSV}")

main_sync_jupyter()
