/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    return new Promise((resolve,reject)=>{
            promise1
                .then((n1)=>{
                    promise2.then(n2=>{
                        resolve(n1+n2)
                    })
                }
                )
    })
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */