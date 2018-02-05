//basically the same as mergesort, but return no. of invertions instead of void.


#include <iostream>


template <typename T>
int merge(T a[], int left, int mid, int right) {
	int count = 0;
	int length = right - left + 1;
	int temp[length];

	int left_next = left;
	int right_next = mid + 1;

	for (int i = 0; i < length; ++i) {
		if (left_next > mid)
			temp[i] = a[right_next++];
		else if (right_next > right)
			temp[i] = a[left_next++];
		else if (a[left_next]<= a[right_next])
			temp[i] = a[left_next++];
		else {
			temp[i] = a[right_next++];
			count += mid-left_next + 1;//when the number on the right is larger
		}
	}

	for (int i = 0; i < length; ++i)
		a[left++] = temp[i];

	return count;
}


template <typename T>
int mergesort(T a[], int left, int right) {
	if (left >= right)
		return 0;
	else {
		int mid = (left + right) / 2;
		int left_i = mergesort(a, left, mid);
		int right_i = mergesort(a, mid + 1, right);
		return left_i + right_i + merge(a, left, mid, right);//better to use 3 or 4 index here?
	}

}



int main() {
	int a[5] = {4, 8, 0, 2, 5};
	int s = mergesort(a, 0, 4);

	for (auto &i: a)
		std::cout << i << " ";
	std::cout << s << std::endl;


	return 0;
}



