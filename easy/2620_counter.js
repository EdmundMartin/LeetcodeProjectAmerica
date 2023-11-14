/**
 * @param {number} n
 * @return {Function} counter
 */
const createCounter = function (n) {
    this.count = n;

    return function () {
        let ret = this.count;
        this.count++;
        return ret;
    };
};