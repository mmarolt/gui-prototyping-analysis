const NUM_APPS = 4;
const NUM_METHODS = 4;
const METHOD = ["instruction", "pd_zs", "pd_fs", "ref_instruction"];
const APPS = [3261, 38961, 53054, 69587];
const CRITERIA = [
    "Skladnost z zahtevami",
    "Ustreznost komponent",
    "Intuitivnost in preprostost",
    "Minimalno število slabosti",
    "Estetska privlačnost",
    "Splošno zadovoljstvo"
];

async function loadDataset() {
    const resp = await fetch('dataset.csv');
    const text = await resp.text();
    const rows = text.trim().split('\n').map(r => r.split(';'));
    const idMap = {};
    const opisMap = {};
    rows.slice(1).forEach(r => {
        idMap[r[0]] = r[1];
        ///opisMap[+r[0]] = r[2];
        opisMap[+r[1]] = r[2];
    });
    return [opisMap, idMap];
}

function createPrototype(index, id) {
    const div = document.createElement("div");
    div.className = "prototype";

    const h3 = document.createElement("h3");
    h3.textContent = `Prototype ${index}`;
    div.appendChild(h3);

    const iframe = document.createElement("iframe");
    iframe.src = `generated_guis_mm/${id}/${METHOD[index-1]}.html`;
    div.appendChild(iframe);

    CRITERIA.forEach((crit, cIndex) => {
        const critDiv = document.createElement("div");
        critDiv.className = "criterion";

        const span = document.createElement("span");
        span.textContent = crit;
        critDiv.appendChild(span);

        const ratingsDiv = document.createElement("div");
        ratingsDiv.className = "ratings-inline";
        for (let i = 1; i <= 5; i++) {
            const label = document.createElement("label");
            label.innerHTML = `<input type="radio" name="p${index}_c${cIndex}" value="${i}" required> ${i}`;
            ratingsDiv.appendChild(label);
        }
        critDiv.appendChild(ratingsDiv);
        div.appendChild(critDiv);
    });

    return div;
}

function createGroup(groupIndex, opis, prototypes) {
    const groupDiv = document.createElement("div");
    groupDiv.className = "group";

    const h2 = document.createElement("h2");
    h2.textContent = `App ${groupIndex + 1}`;
    groupDiv.appendChild(h2);

    const p = document.createElement("p");
    p.textContent = opis || "Opis sklopa ni na voljo.";
    groupDiv.appendChild(p);

    prototypes.forEach(proto => groupDiv.appendChild(proto));
    return groupDiv;
}

loadDataset().then(([opisMap, idMap]) => {
    const groupsDiv = document.getElementById("groups");
    for (let g = 0; g < NUM_APPS; g++) {
        const prototypes = [];
        const appId = APPS[g];
        for (let i = 1; i <= NUM_METHODS; i++) {
            ///prototypes.push(createPrototype(i, idMap[i]));
            prototypes.push(createPrototype(i, appId));
        }

        ///const opis = opisMap[g + 1]; // v dataset.csv so lahko opisi po sklopih (1–5)
        const opis = opisMap[appId];
        groupsDiv.appendChild(createGroup(g, opis, prototypes));
    }
});

document.getElementById("surveyForm").addEventListener("submit", function(e) {
    e.preventDefault();
    const formData = new FormData(e.target);
    const data = {};
    formData.forEach((val, key) => { data[key] = val; });

    let csv = "key,value\n";
    for (let k in data) {
        csv += `${k},${data[k]}\n`;
    }

    const blob = new Blob([csv], { type: "text/csv" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "results.csv";
    a.click();
    URL.revokeObjectURL(url);
});