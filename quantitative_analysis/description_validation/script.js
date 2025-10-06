const APPS = ['12740', '14283', '18782', '20947', '22151', '27360', '27382', '27707', '30982', '31390', '32310', '3261', '33383', '34346', '34517', '34527', '35526', '3727', '37505', '38961', '40673', '43872', '43977', '44756', '47926', '49794', '53054', '53469', '54377', '54468', '56905', '58124', '59429', '59576', '61851', '63575', '64858', '65592', '67044', '68368', '69574', '69587', '70410', '8640'];
const NUM_APPS = 44;
const METHOD = ["instruction", "pd_zs", "pd_fs", "ref_instruction"];

function splitOpisToSentences(opis) {
    return opis.split('.').map(s => s.trim()).filter(s => s.length > 0);
}

async function loadDataset() {
    const resp = await fetch('../../dataset.csv');
    const text = await resp.text();
    const rows = text.trim().split('\n').map(r => r.split(';'));
    const opisMap = {};
    rows.slice(1).forEach(r => {
        opisMap[+r[0]] = r[1];
    });
    return opisMap;
}

function createPrototype(appId, methodIndex, opis) {
    const div = document.createElement("div");
    div.className = "prototype-block";

    // Leva stran: prototip (iframe)
    const iframe = document.createElement("iframe");
    iframe.src = `../../generated_guis/${appId}/${METHOD[methodIndex]}.html`;
    iframe.width = "375";
    iframe.height = "667";
    iframe.className = "prototype-iframe";
    div.appendChild(iframe);

    // Desna stran: opis z checkboxi
    const opisDiv = document.createElement("div");
    opisDiv.className = "opis-block";
    opisDiv.innerHTML = `<strong>Opis aplikacije:</strong>`;
    const sentences = splitOpisToSentences(opis);

    sentences.forEach((stavek, idx) => {
        const lineDiv = document.createElement("div");
        lineDiv.className = "opis-line";

        const checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.name = `a${appId}_m${methodIndex}_s${idx}`;
        checkbox.value = "1";

        const label = document.createElement("label");
        label.textContent = stavek;

        lineDiv.appendChild(checkbox);
        lineDiv.appendChild(label);
        opisDiv.appendChild(lineDiv);
    });

    div.appendChild(opisDiv);
    return div;
}

function createGroup(appIndex, opis) {
    const groupDiv = document.createElement("div");
    groupDiv.className = "group-block";

    const h2 = document.createElement("h2");
    h2.textContent = `App ${appIndex + 1}`;
    groupDiv.appendChild(h2);

    for (let m = 0; m < METHOD.length; m++) {
        groupDiv.appendChild(createPrototype(APPS[appIndex], m, opis));
    }
    return groupDiv;
}

document.addEventListener("DOMContentLoaded", async function() {
    const opisMap = await loadDataset();
    const groupsDiv = document.getElementById("groups");
    for (let g = 0; g < NUM_APPS; g++) {
        const appId = APPS[g];
        const opis = opisMap[appId] || "Opis ni na voljo.";
        groupsDiv.appendChild(createGroup(g, opis));
    }

    document.getElementById("surveyForm").addEventListener("submit", function(e) {
        e.preventDefault();
        const formData = new FormData(e.target);

        let csvContent = "UI_Number;Method;All;Correct\n";

        for (let g = 0; g < NUM_APPS; g++) {
            const appId = APPS[g];
            const opis = opisMap[appId] || "";
            const sentences = splitOpisToSentences(opis);

            for (let m = 0; m < METHOD.length; m++) {
                let checkedCount = 0;
                for (let s = 0; s < sentences.length; s++) {
                    const key = `a${appId}_m${m}_s${s}`;
                    if (formData.has(key)) checkedCount++;
                }
                csvContent += `${appId};${METHOD[m]};${sentences.length};${checkedCount}\n`;
            }
        }

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
});