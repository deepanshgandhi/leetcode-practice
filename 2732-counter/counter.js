/**
 * @param {number} n
 * @return {Function} counter
 */
function createCounter(n){
    count = n;
    return function(){
        return count++;
    }
}

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */