#include <iostream>
using namespace std;

template <typename Type>
Type sum(Type a[], int n)
{
	Type sum = 0;

	for (int i = 0; i < n; i++)
		sum += a[i];

	return sum;
}

template <typename T>		// 함수 템플릿으로 정의
void print_array(T a[], int n)
{
	for (int i = 0;i < n; i++)
		cout << a[i] << " ";
	cout << endl;
}


template <>		// 템플릿 특수화
void print_array(char* a, int n)	// 매개 변수가 char인 경우에는 이 함수가 호출된다.
{
	cout << a << endl;
}

int main()
{
	int a[] = { 10,20, 30, 40, 50, 60 };
	char b[] = { 'a', 'b', 'c', 'd', 'e', '\0' };
	double c[] = { 10.1, 10.4, 14.6, 20.1, 6.4 };

	print_array(a, 6);
	print_array(b, 6);
	cout << sum(a, 6) << " " << sum(c, 5) << endl;

	return 0;
}