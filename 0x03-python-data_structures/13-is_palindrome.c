#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

/**
 * is_palindrome- Checks if a singly linked list is a palindrome.
 * @head: Head pointer
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *node;
	int node_data[9999], idx = 0, front_idx = 0;

	if ((!*head) || (!head))
	{
		return (1);
	}
	node = *head;
	if (!node->next)
	{
		return (1);
	}
	while (node)
	{
		node_data[idx] = node->n;
		node = node->next;
		idx++;
	}
	idx--;
	while (idx >= 0 && front_idx <= idx)
	{
		if (node_data[idx] != node_data[front_idx])
		{
			return (0);
		}
		idx--;
		front_idx++;
	}
	return (1);
}
