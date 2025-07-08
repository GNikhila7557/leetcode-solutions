class ArrayWrapper {
    constructor(nums) {
        this.nums = nums;
    }

    valueOf() {
        return this.nums.reduce((sum, val) => sum + val, 0);
    }

    toString() {
        return `[${this.nums.join(",")}]`;
    }
}