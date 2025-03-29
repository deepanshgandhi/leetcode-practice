/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let curr = init;
    const increment = () => {
        return ++curr;
    };
    const decrement = () => {
        return --curr;
    }
    const reset = () => {
        curr = init;
        return curr;
    };
    return {
        increment : increment,
        decrement : decrement,
        reset : reset
    };
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */