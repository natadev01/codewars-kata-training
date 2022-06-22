const runLengthEncoding = str => {  
  let arr_str = str.split('');
  let count=1;
  let e=0;
  let new_arr = []
  if (str == ''){
    return [];
  }
  arr_str.map( a => { (e === 0)? (a === arr_str[e+1])? count+=1 : new_arr.push([count, a]): (a === arr_str[e+1])? count+=1: new_arr.push([ count, a]);
    if (a !== arr_str[e+1]) {
        count=1;
    }
      e++;
    }
  )
  return new_arr // << fix this
}
console.log(runLengthEncoding('lalaaa223ttltt'))