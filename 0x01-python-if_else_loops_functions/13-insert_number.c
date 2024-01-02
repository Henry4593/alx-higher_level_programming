#include "lists.h"
#include <stdlib.h>

/**
  * insert_node - inserts a number into a sorted singly linked list and returns
  * the updated list
  * @head: head of the sorted singly linked list
  * @number: the number to be inserted on the linked list
  *
  * Return: the updated of the sorted singly linked list
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node = NULL, *new_node = NULL, *temp_node = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	if (*head)
	{
		current_node = *head;
		if (number <= current_node->n)
		{
			new_node->next = current_node;
			*head = new_node;
		}
		else
		{
			while (current_node->next)
			{
				if (number <= current_node->next->n)
				{
					temp_node = current_node->next;
					current_node->next = new_node;
					new_node->next = temp_node;
					return (*head);
				}

				current_node = current_node->next;
			}
			temp_node = current_node->next;
			current_node->next = new_node;
			new_node->next = temp_node;
		}
		return (*head);
	}
	new_node->next = NULL;
	*head = new_node;
	return (*head);
}
