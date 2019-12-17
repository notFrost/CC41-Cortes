const reader = new FileReader()

let createTextElement = (doc, element, text) => {
}

let selectData = (minerals) => {
    let selectList = document.createElement("select");
    selectList.size = "15";

    minerals.forEach(element => {
        if (element.includes("_ppm")) {
            let el = document.createElement("option");
            el.value = element;
            el.text = element;
            console.log(element);
            selectList.appendChild(el);
        }
    });
    let selectData = document.getElementById("selectId");
    let title = document.createElement("h2");
    let t = document.createTextNode("Geoquimica     Correlacionar");
    title.appendChild(t);                                   // Append the text to <h1>
    selectData.appendChild(title);
    selectData.appendChild(selectList);
    // creating button element  
    let button = document.createElement('BUTTON');
    let text = document.createTextNode("Add -->");
    button.appendChild(text);
    selectData.appendChild(button);

    button = document.createElement('BUTTON');
    text = document.createTextNode("<-- Remove");
    button.appendChild(text);
    selectData.appendChild(button);


    selectList = document.createElement("select");
    selectList.size = "15";
    selectData.appendChild(selectList);
}


const readText = (that) => {
    if (that.files && that.files[0]) {
        let reader = new FileReader();
        reader.onload = (e) => {
            let output = e.target.result;
            //process text to show only lines with "@":				
            output = output.split("\n").filter(/./.test, /\;/).join("\n");
        };//end onload()
        reader.readAsText(that.files[0]);
        Papa.parse(that.files[0], {
            complete: (results) => {
                selectData(results.data[0])
            }
        });
    }//end if html5 filelist support
}

