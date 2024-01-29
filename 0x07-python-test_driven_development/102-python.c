#include "Python.h"

/**
 * print_python_string - Prints basic info of a Python string object
 * @p: A pointer to the Python string object
 *
 * Description: Checks that p is a valid Python string object.
 * Prints type (compact ascii vs unicode), length, and value.
 * Uses macros to access internal string size and data.
 * Converts string to wide char string before printing.
 * Prints error message if invalid string object.
 *
 * Returns: None
 */

void print_python_string(PyObject *p)
{
	long int length;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	length = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
