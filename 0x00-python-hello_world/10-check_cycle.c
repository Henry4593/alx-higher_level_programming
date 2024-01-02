#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: The singly linked list to be checked
 *
 * Return: 1 if there is a cycle in the list, 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *is_slow_ptr = list, *is_fast_ptr = list;
	int has_cycle = 0;

	while ((is_slow_ptr && is_fast_ptr) && is_fast_ptr->next)
	{
		is_slow_ptr = is_slow_ptr->next;
		is_fast_ptr = is_fast_ptr->next->next;

		if (is_slow_ptr == is_fast_ptr)
		{
			has_cycle = 1;
			break;
		}
	}

	return (has_cycle);
}

