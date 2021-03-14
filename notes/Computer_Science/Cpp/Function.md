---
title: Function
---

## Argument Passing

By default, arguments are pass by value copying the input to the argument varaible.

### Pass by Reference

To not copy the input, use pass-by-reference by modifying the argument to be `&arg`.

```cpp
void f(vector<int> &v) {

}
```

### Immutable

If an argument is mutable but you'd like to indicate that it should be immutable inside the function/local scope, you can modify the argument to be `const arg`.

It is very common to see `const` applied to pass-by-reference rather than pass-by-value.

## Return Value

By default, object are return-by-value meaning the object return are copied.

```cpp
vector copy(const vector<int> &v) {
	vector p;

	for (i=1; i < sizeof(v); ++i) {
		p[i] = &v[i];
	}

	return p;
}
```

### Return by Pointer

This is not recommended. To prevent return-by-value, one may have the pointer return instead:

```cpp
vector* copy(const vector<int> &v) {
	vector* p = new vector;

	for (i=1; i < sizeof(v); ++i) {
		p[i] = &v[i];
	}

	return p;
}
```

### Return by Reference

**Never do this!** The reference will point to nonsense because the local scope may disappear.

```cpp
vector& copy(const vector<int> &v) {
	vector rv = new vector;

	for (i=1; i < sizeof(v); ++i) {
		p[i] = &v[i];
	}

	return rv;
}
```
