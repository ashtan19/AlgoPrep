function longestString(strArr) {
  let maxLenIndex = 0;
  let maxLen = 0;
  for (let i = 0; i < strArr.length; i++) {
    if (strArr[i].length > maxLen) {
      maxLen = strArr[i].length;
      maxLenIndex = i;
    }
  }

  return strArr[maxLenIndex];
}

function alphabetShift(str) {
  let result = [];
  for (let i = 0; i < str.length; i++) {
    let curCharCode = str.charCodeAt(i);
    if (curCharCode === "z".charCodeAt(0)) {
      result.push("a");
    } else {
      const nextChar = String.fromCharCode(curCharCode + 1);
      result.push(nextChar);
    }
  }

  return result.join("");
}

function kthGreatest(arr, k) {
  //Could use a heap but there is no built in support in js
  arr.sort(function (a, b) {
    return a - b;
  });
  return arr[arr.length - k];
}

function twoPartSum(arr) {
  let sum1 = 0;
  let sum2 = 0;
  for (let i = 0; i < arr.length; i++) {
    if (i % 2 === 0) {
      sum1 += arr[i];
    } else {
      sum2 += arr[i];
    }
  }

  return [sum1, sum2];
}

function rearrangeChar(str1, str2) {
  const sorted1 = str1.split("").sort().join("");
  const sorted2 = str2.split("").sort().join("");
  if (sorted1 === sorted2) {
    return 1;
  } else {
    return 0;
  }
}
