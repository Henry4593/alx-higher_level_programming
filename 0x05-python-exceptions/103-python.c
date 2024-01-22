#include "/usr/include/python3.4m/Python.h"
#include <stdio.h>
#include <stdlib.h>

void print_hex_num(const char *str, int num);
void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

void print_hex_num(const char *str, int num)
{
	int idx = 0;

	for (; idx < num - 1; ++idx)
		printf("%02x ", (unsigned char) str[idx]);

	printf("%02x", str[idx]);
    fflush(stdout);
}

void print_python_bytes(PyObject *p)
{
    PyBytesObject *duplicate = (PyBytesObject *) p;
	int calc_bytes, duplicate_size = 0;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    duplicate_size = PyBytes_Size(p);
    calc_bytes = duplicate_size + 1;

    if (calc_bytes >= 10)
        calc_bytes = 10;

    printf("  size: %d\n", duplicate_size);
    printf("  trying string: %s\n", duplicate->ob_sval);
    printf("  first %d bytes: ", calc_bytes);
    print_hex_num(duplicate->ob_sval, calc_bytes);
    printf("\n");

    fflush(stdout);
}

void print_python_list(PyObject *p)
{   
    int idx = 0, list_length = 0;
	PyObject *item;
	PyListObject *duplicate = (PyListObject *) p;

    printf("[*] Python list info\n");
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

	list_length = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %d\n", list_length);
	printf("[*] Allocated = %d\n", (int) duplicate->allocated);

	for (; idx < list_length; ++idx)
	{
		item = PyList_GET_ITEM(p, idx);
		printf("Element %d: %s\n", idx, item->ob_type->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
        else if (PyFloat_Check(item))
            print_python_float(item);
	}

    fflush(stdout);
}

void print_python_float(PyObject *p)
{
    PyFloatObject *duplicate = (PyFloatObject *) p;
    float num = 0;

    printf("[.] float object info\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    num = duplicate->ob_fval;

    if ((int) num == num)
        printf("  value: %0.1f\n", duplicate->ob_fval);
    else
        printf("  value: %0.16g\n", duplicate->ob_fval);

    fflush(stdout);
}
