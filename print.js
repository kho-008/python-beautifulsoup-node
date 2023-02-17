const _ = require('lodash');
const data = require('./output.json');

let keyList = []
data.map((cur) => {
  keyList.push(Object.keys(cur))
  
  _(cur).keys().sort().pickBy(function(key) {
    return key !== 'size' && key !== 'rows' && key !== 'cols' && cur[key] !== '';
  })
  .each(function (key) {
    const value = Array.isArray(cur[key]) ? `.${cur[key].join('.')}` : cur[key]
    console.log(key, value);
  });
})

console.log(_.uniq(keyList.flat()))