#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A pointer to a PyObject representing a List Object.
 * It should point to an instance of the PyListObject structure.
 * Description: This function prints information about a Python List Object,
 * including its size and allocated memory, and information about the elements
 * it contains.
 *
 * Return: Nothing
 */

void print_python_list(PyObject *p)
{
	int size, alloc_mem, idx;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	alloc_mem = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc_mem);

	for (idx = 0; idx < size; idx++)
	{
		type = list->ob_item[idx]->ob_type->tp_name;
		printf("Element %d: %s\n", idx, type);
		if (strcmp(type, "bytes") == 0)
		{
			print_python_bytes(list->ob_item[idx]);
		}
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A pointer to a PyObject representing a Bytes Object.
 * Description: It should point to an instance of the PyBytesObject structure.
 * Return: Nothing
 */

void print_python_bytes(PyObject *p)
{
	unsigned char idx, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);
	if (((PyVarObject *)p)->ob_size > 10)
	{
		size = 10;
	}
	else
	{
		size = ((PyVarObject *)p)->ob_size + 1;
	}
	printf("  first %d bytes: ", size);
	for (idx = 0; idx < size; idx++)
	{
		printf("%02hhx", bytes->ob_sval[idx]);
		if (idx == (size - 1))
		{
			printf("\n");
		}
		else
		{
			printf(" ");
		}
	}
}
