package twosum

import "testing"

func Test(t *testing.T) {
	cases := []struct {
		arr  []int
		k    int
		want bool
	}{
		{[]int{10, 15, 3, 7}, 17, true},
		{[]int{1, 2, 3, 4}, 10, false},
		{[]int{}, 10, false},
		{[]int{1}, 1, false},
		{[]int{1, 2}, 3, true},
	}

	for _, c := range cases {
		var result = isSumInArray(c.arr, c.k)
		if result != c.want {
			t.Errorf("Expected %t, got %t", c.want, result)
		}
	}
}
