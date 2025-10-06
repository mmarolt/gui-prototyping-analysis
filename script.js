const NUM_APPS = 44;
const NUM_METHODS = 4;
const METHOD = ["instruction", "pd_zs", "pd_fs", "ref_instruction"];
const APPS = ['12740', '14283', '18782', '20947', '22151', '27360', '27382', '27707', '30982', '31390', '32310', '3261', '33383', '34346', '34517', '34527', '35526', '3727', '37505', '38961', '40673', '43872', '43977', '44756', '47926', '49794', '53054', '53469', '54377', '54468', '56905', '58124', '59429', '59576', '61851', '63575', '64858', '65592', '67044', '68368', '69574', '69587', '70410', '8640'];
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
        //idMap[r[0]] = r[1];
        //opisMap[+r[0]] = r[2];
        opisMap[+r[0]] = r[1];
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

/*document.getElementById("surveyForm").addEventListener("submit", async function(e) {
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
});*/

document.getElementById("surveyForm").addEventListener("submit", function(e) {
    console.log("Submit handler je sprožen!");
    e.preventDefault();
    const formData = new FormData(e.target);
    const data = {};
    formData.forEach((val, key) => { data[key] = val; });

    const keys = Object.keys(data);
    const values = Object.values(data);

    let csvContent = keys.join(";") + "\n";
    csvContent += values.map(v => `"${v.replace(/"/g, '""')}"`).join(";") + "\n";

    const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
    const url = URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = "rezultati.csv";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);

    URL.revokeObjectURL(url);

    alert("Rezultati so bili preneseni kot CSV datoteka.");
});