


#include <iostream>


template <typename T>
void merge(T a[], int left, int mid, int right) {
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
		else
			temp[i] = a[right_next++];
	}

	for (int i = 0; i < length; ++i)
		a[left++] = temp[i];

}


template <typename T>
void mergesort(T a[], int left, int right) {
	if (left >= right)
		return;
	else {
		int mid = (left + right) / 2;
		mergesort(a, left, mid);
		mergesort(a, mid + 1, right);
		merge(a, left, mid, right);//better to use 3 or 4 index here?
	}

}



int main() {
	char a[5] = {'e', 'a', 't', 's', 'k'};
	mergesort(a, 0, 4);

	for (auto &i: a)
		std::cout << i << " ";
	std::cout << std::endl;


	return 0;
}



