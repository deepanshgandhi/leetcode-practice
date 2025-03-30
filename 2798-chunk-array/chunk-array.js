/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr,size){
    const res = [];
    let sub = [];
    for(let i=0; i<arr.length;i++){
        sub.push(arr[i])
        if(sub.length===size){
            res.push(sub)
            sub = []
        }
    }
    if(sub.length > 0)
        res.push(sub)
    return res
}
