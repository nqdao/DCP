package twosum

func isSumInArray(arr []int, k int) bool {
	for i, value := range arr {
		comp := k - value
		for j := i + 1; j < len(arr); j++ {
			if arr[j] == comp {
				return true
			}
		}
	}
	return false
}
