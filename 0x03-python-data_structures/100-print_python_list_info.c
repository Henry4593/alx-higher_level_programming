#include <Python.h>
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

/**
 * print_python_list_info- Prints some basic info about Python lists.
 * @p: pointer to type PyObject
 */

void print_python_list_info(__attribute__((unused)) PyObject * p)
{
	int idx_trav;

	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (idx_trav = 0; idx_trav < Py_SIZE(p); idx_trav++)
	{
		printf("Element %d: %s\n", idx_trav,
				Py_TYPE(PyList_GetItem(p, idx_trav))->tp_name);
	}
}
