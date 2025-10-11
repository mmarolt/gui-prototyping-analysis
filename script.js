const NUM_APPS = 12;
const NUM_METHODS = 4;
const METHOD = ["instruction", "pd_zs", "pd_fs", "ref_instruction"];
const APPS = ['8640','12740','22151','27382','31390','34527','38961','43977','44756','59429','59576','69574'];
const CRITERIA = [
    "Prototip je skladen s svojim opisom. ",
    "Komponente so pravilno izbrane, jasno poimenovane in logično umeščene. ",
    "Uporabnik brez dodatnih navodil razume, kako uporabljati prototip. ",
    "V prototipu ni oblikovalskih ali funkcionalnih napak. ",
    "Prototip je vizualno usklajen, prijeten in profesionalen. ",
    "Generalno gledano, je vmesnik dober. "
];

async function loadDataset() {
    const resp = await fetch('dataset.csv');
    const text = await resp.text();
    const rows = text.trim().split('\n').map(r => r.split(';'));
    const idMap = {};
    const opisMap = {};
    rows.slice(1).forEach(r => {
        opisMap[+r[0]] = r[1];
    });
    return [opisMap, idMap];
}

function createPrototype(index, id) {
    const div = document.createElement("div");
    div.className = "prototype";

    const h3 = document.createElement("h3");
    h3.textContent = `Prototip ${index}`;
    div.appendChild(h3);

    const iframe = document.createElement("iframe");
    iframe.src = `generated_guis/${id}/${METHOD[index-1]}.html`;
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
            //input.required = true;

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
    h2.textContent = `Opis aplikacije ${groupIndex + 1}`;
    groupDiv.appendChild(h2);

    const p = document.createElement("p");
    p.textContent = opis || "Opis sklopa ni na voljo.";
    groupDiv.appendChild(p);

    prototypes.forEach(proto => groupDiv.appendChild(proto));
    return groupDiv;
}

loadDataset().then(([opisMap]) => {
    const groupsDiv = document.getElementById("groups");
    for (let g = 0; g < NUM_APPS; g++) {
        const prototypes = [];
        const appId = APPS[g];
        for (let i = 1; i <= NUM_METHODS; i++) {
            prototypes.push(createPrototype(i, appId));
        }

        const opis = opisMap[appId];
        groupsDiv.appendChild(createGroup(g, opis, prototypes));
    }
});

document.getElementById("surveyForm").addEventListener("submit", async function(e) {
    const answers = [];
    ids.forEach(id => {
        indexes.forEach(index => {
            cIndexes.forEach(cIndex => {
                const name = `a${id}_p${index}_c${cIndex}`;
                const checked = document.querySelector(`input[name="${name}"]:checked`);
                answers.push({
                    name: name,
                    value: checked ? checked.value : ""
                });
            });
        });
    });
    // Shrani kot CSV
    const csv = answers.map(a => `${a.name},${a.value}`).join("\n");
    document.getElementById("odgovori").value = csv;

    alert("Hvala! Odgovori so bili shranjeni.");
});