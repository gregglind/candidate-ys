
const csv =require("csvtojson");
const OUTFILENAME = "./artefacts/pollution.csv"

async function unpack () {
    console.log("OK. Done unpacking.")  
    return "../downloads/US_2019/sample.US_1a_2019.txt";
}


// 1.  Parse the data from local / downloads folder
async function parse(loc) {
    // data comes as a zip of txt files.
    // FIXME:  glind.  pretend these are already in `../downloads/US_2019.zip`
    debugger;
    const jsonArray = await csv().fromfile(loc);
    return jsonArray;
}

// 2.  Aggregate
async function aggregate() {
    return [{"Company": "APolluter", "Amount-tons": 131.13, "Locations": [], "Chemicals": [] }]
}

async function ouptut (answer, location) {
}

// 
async function transform() {
    debugger;
    const loc = await unpack();
    const arr = await parse(loc);
    const answer = await aggregate(arr);
    output(answer, OUTFILENAME)
}

transform();

exports = {
    transform
};