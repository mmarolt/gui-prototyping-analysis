const APPS = ['12740', '14283', '18782', '20947', '22151', '27360', '27382', '27707', '30982', '31390', '32310', '3261', '33383', '34346', '34517', '34527', '35526', '3727', '37505', '38961', '40673', '43872', '43977', '44756', '47926', '49794', '53054', '53469', '54377', '54468', '56905', '58124', '59429', '59576', '61851', '63575', '64858', '65592', '67044', '68368', '69574', '69587', '70410', '8640'];
const NUM_APPS = 44;
const METHOD = ["instruction", "pd_zs", "pd_fs", "ref_instruction"];

function createPrototype(appId, methodIndex) {
    const div = document.createElement("div");
    div.className = "prototype-block";

    // Leva stran: prototip (iframe)
    const iframe = document.createElement("iframe");
    iframe.src = `../../generated_guis/${appId}/${METHOD[methodIndex]}.html`;
    iframe.width = "600";
    iframe.height = "400";
    iframe.className = "prototype-iframe";
    div.appendChild(iframe);

    // Desna stran: inputi za ocenjevanje
    const inputDiv = document.createElement("div");
    inputDiv.className = "input-block";

    // Vnos števila elementov izven dimenzij
    const row1 = document.createElement("div");
    row1.className = "input-row";
    const label1 = document.createElement("label");
    label1.textContent = "Število elementov izven dimenzij:";
    const input1 = document.createElement("input");
    input1.type = "number";
    input1.min = "0";
    input1.name = `a${appId}_m${methodIndex}_out_of_bounds`;
    input1.value = "";
    input1.required = true;
    row1.appendChild(label1);
    row1.appendChild(input1);

    // Vnos števila neodzivnih elementov
    const row2 = document.createElement("div");
    row2.className = "input-row";
    const label2 = document.createElement("label");
    label2.textContent = "Število neodzivnih elementov:";
    const input2 = document.createElement("input");
    input2.type = "number";
    input2.min = "0";
    input2.name = `a${appId}_m${methodIndex}_nonresponsive`;
    input2.value = "";
    input2.required = true;
    row2.appendChild(label2);
    row2.appendChild(input2);

    // Vnos števila elementov, ki se prekrivajo (niso prikazani v celoti)
    const row3 = document.createElement("div");
    row3.className = "input-row";
    const label3 = document.createElement("label");
    label3.textContent = "Število prekritih elementov:";
    const input3 = document.createElement("input");
    input3.type = "number";
    input3.min = "0";
    input3.name = `a${appId}_m${methodIndex}_hidden`;
    input3.value = "";
    input3.required = true;
    row3.appendChild(label3);
    row3.appendChild(input3);

    // Vnos števila elementov z neberljivim tekstom
    const row4 = document.createElement("div");
    row4.className = "input-row";
    const label4 = document.createElement("label");
    label4.textContent = "Število neberljivih elementov z besedilom:";
    const input4 = document.createElement("input");
    input4.type = "number";
    input4.min = "0";
    input4.name = `a${appId}_m${methodIndex}_unreadable`;
    input4.value = "";
    input4.required = true;
    row4.appendChild(label4);
    row4.appendChild(input4);

    // Vnos števila neustreznih/neprikazanih ikon
    const row5 = document.createElement("div");
    row5.className = "input-row";
    const label5 = document.createElement("label");
    label5.textContent = "Število neustreznih ikon:";
    const input5 = document.createElement("input");
    input5.type = "number";
    input5.min = "0";
    input5.name = `a${appId}_m${methodIndex}_icons`;
    input5.value = "";
    input5.required = true;
    row5.appendChild(label5);
    row5.appendChild(input5);

    // Checkbox: GUI ni ustrezne dimenzije
    const row6 = document.createElement("div");
    row6.className = "input-row";
    const input6 = document.createElement("input");
    input6.type = "checkbox";
    input6.name = `a${appId}_m${methodIndex}_dimensions`;
    input6.value = "1";
    const label6 = document.createElement("label");
    label6.textContent = "GUI ni ustrezne dimenzije";
    row6.appendChild(input6);
    row6.appendChild(label6);

    // Dodaj vse vrstice v input blok
    inputDiv.appendChild(row1);
    inputDiv.appendChild(row2);
    inputDiv.appendChild(row3);
    //inputDiv.appendChild(row4);
    //inputDiv.appendChild(row5);
    inputDiv.appendChild(row6);

    div.appendChild(inputDiv);
    return div;
}

function createGroup(appIndex) {
    const groupDiv = document.createElement("div");
    groupDiv.className = "group-block";

    const h2 = document.createElement("h2");
    h2.textContent = `App ${APPS[appIndex]}`;
    groupDiv.appendChild(h2);

    for (let m = 0; m < METHOD.length; m++) {
        groupDiv.appendChild(createPrototype(APPS[appIndex], m));
    }
    return groupDiv;
}

document.addEventListener("DOMContentLoaded", async function() {
    const groupsDiv = document.getElementById("groups");
    for (let g = 0; g < NUM_APPS; g++) {
        groupsDiv.appendChild(createGroup(g));
    }

    document.getElementById("surveyForm").addEventListener("submit", function(e) {
        e.preventDefault();
        const formData = new FormData(e.target);

        // Pripravi CSV glavo
        let csvContent = "UI_Number;Method;Bounds;Nonresponsive;Hidden;Dimensions\n";

        for (let g = 0; g < NUM_APPS; g++) {
            const appId = APPS[g];
            for (let m = 0; m < METHOD.length; m++) {
                const outOfBounds = formData.get(`a${appId}_m${m}_out_of_bounds`) || "0";
                const nonresponsive = formData.get(`a${appId}_m${m}_nonresponsive`) || "0";
                const hidden = formData.get(`a${appId}_m${m}_hidden`) || "0";
                const unreadable = formData.get(`a${appId}_m${m}_unreadable`) || "0";
                const icons = formData.get(`a${appId}_m${m}_icons`) || "0";
                const dimensions = formData.has(`a${appId}_m${m}_dimensions`) ? "YES" : "NO";
                csvContent += `${appId};${METHOD[m]};${outOfBounds};${nonresponsive};${hidden};${dimensions}\n`;
            }
        }

        const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
        const url = URL.createObjectURL(blob);

        const a = document.createElement("a");
        a.href = url;
        a.download = "gui_visual_analysis.csv";
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);

        alert("Rezultati so bili preneseni kot CSV datoteka.");
    });
});