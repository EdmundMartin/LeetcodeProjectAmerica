/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
	let total = 0;
    for (const arg of args) {
	    total += 1;
    }
    return total;
};