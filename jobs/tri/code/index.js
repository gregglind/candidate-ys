#!/usr/bin/node

const cheerio = require('cheerio');
const puppeteer = require('puppeteer');
const assert = require('assert');

const {transform} = require("./transform");
/** 
# Module notes and roadblocks

## Code notes.

In a "real" system, this would
- log
- have tests
- actually do all the unzipping etc during parse


## Roadblocks

- Starting URL isn't stable.  It will look something like this:
https://www.epa.gov/toxics-release-inventory-tri-program/tri-basic-plus-data-files-calendar-years-1987-2019?
- Unknown update schedule.  We don't know the schedule under which this updates.
- Unstable selectors.  starting url page is a constructed page in a CMS system
*/

// 1. Download the data.
async function download() {
  const STARTINGURL = "https://www.epa.gov/toxics-release-inventory-tri-program/tri-data-and-tools";
  const SELECTOR_BUTTON = "#pane-9 > form" // WARNING:  selector is fragile

  const browser = await puppeteer.launch({headless:false}); // default is true
  const page = await browser.newPage();

  let form;
  
  // Find the form that goes all data
  await page.goto(STARTINGURL);
  await page.waitForSelector(SELECTOR_BUTTON);
  form = await page.$(SELECTOR_BUTTON);
  await form.evaluate( form => form.submit() );
  await page.waitForNavigation();

  debugger;

  assert(page.url().match("https://www.epa.gov/toxics-release-inventory-tri-program/tri-basic-plus-data-files-calendar-years"), "All data page doesn't match expected url")

  debugger;
  // Page 2:  download the "everything"
  const SELECTOR_ALLDATA = "#open_link";
  form = page.waitForSelector(SELECTOR_ALLDATA);
  
  // fix glind.  push the button, doesn't quite work
  //await form.evaluate( form => form.submit() );
  
  console.log("files downloaded.  (simulated)")

  // close browser
  await browser.close();
}


async function main() {
  await download()
  await parse()
  await output()  
}
main();