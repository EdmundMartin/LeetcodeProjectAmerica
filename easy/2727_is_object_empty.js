

/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    let count = 0;
    for (const prop in obj) {
        count++
    }
    return count === 0
};