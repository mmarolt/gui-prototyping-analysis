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

    CRITERIA.forEach((crit) => {
        const cIndex = CRITERIA.indexOf(crit);

        const critDiv = document.createElement("div");
        critDiv.className = "criterion";

        const span = document.createElement("span");
        span.textContent = crit;
        critDiv.appendChild(span);

        const ratingsDiv = document.createElement("div");
        ratingsDiv.className = "ratings-inline";
        for (let i = 5; i >= 1; i--) {
            const input = document.createElement("input");
            input.type = "radio";
            input.id = `a${id}_p${index}_c${cIndex}_${i}`;
            input.name = `a${id}_p${index}_c${cIndex}`;
            input.value = i;
            input.required = true;

            const label = document.createElement("label");
            label.htmlFor = input.id;
            label.className = "star";
            label.textContent = "★";

            ratingsDiv.appendChild(input);
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

document.getElementById("surveyForm").addEventListener("submit", async function(e) {
    e.preventDefault();
    const formData = new FormData(e.target);
    const data = {};
    formData.forEach((val, key) => { data[key] = val; });

    try {
        const resp = await fetch("/netlify/functions/saveResponse", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data),
        });
        if (resp.ok) {
            alert("Hvala! Odgovori so bili shranjeni.");
        } else {
            alert("Napaka pri shranjevanju.");
        }
    } catch (err) {
        alert("Težava s povezavo: " + err);
    }
});