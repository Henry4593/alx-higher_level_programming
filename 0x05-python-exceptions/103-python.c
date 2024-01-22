#include <Python.h>
#include <stdio.h>


/**
* print_python_float - Prints info about a Python float object
* @p: Pointer to the Python float object
*
* Description: Checks if p is a valid Python float.
* Gets the double value from the internal PyFloatObject.
* Converts the value to a string using Python's method.
* Prints the float value along with a info header.
* Handles invalid objects.
*
* Returns: None
*/

void print_python_float(PyObject *p)
{
	double value_lf = 0;
	char *string_lf = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	value_lf = ((PyFloatObject *)p)->ob_fval;
	string_lf = PyOS_double_to_string(value_lf, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", string_lf);
}

/**
 * print_python_bytes - Prints info about a Python bytes object
 * @p: Pointer to the Python bytes object
 *
 * Description: Checks that p is a valid bytes object.
 * Prints size and first 10 bytes of object.
 * Gets bytes content with macro into string.
 * Prints error message if invalid object.
 *
 * Returns: None
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, idx = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	string = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", string);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	while (idx < size + 1 && idx < 10)
	{
		printf(" %02hhx", string[idx]);
		idx++;
	}
	printf("\n");
}

/**
 * print_python_list - Prints basic info of a Python list object
 * @p: A pointer to the Python list object
 *
 * Description: Checks if p is a valid Python list object.
 * Prints the size, allocated bytes, and contained item types.
 * Loops through each item in list, printing the type.
 * Calls helper functions to print more info for float/byte items.
 * Prints error message if p is an invalid list object.
 *
 * Returns: None
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *item;
	int idx_i = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		size = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (idx_i < size)
		{
			item = PyList_GET_ITEM(p, idx_i);
			printf("Element %d: %s\n", idx_i, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFloat_Check(item))
				print_python_float(item);
			idx_i++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
