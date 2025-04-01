/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve,reject)=>{
        const res = new Array(functions.length)
        let ct =0;
        for(let i=0;i<functions.length;i++){
            functions[i]()
                .then((value)=>{
                    res[i] = value;
                    ct++;
                    if(ct===functions.length)
                        resolve(res)
                })
                .catch((error)=>reject(error))
        }
    })
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */