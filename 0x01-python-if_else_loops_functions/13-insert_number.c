#include "lists.h"

/*
 * insert_node - inserts number
 * @head: head
 * @number: number
 * Return: value
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *max;

	max = malloc(sizeof(listint_t));
	if (max == NULL)
		return (NULL);
	max->n = number;

	if (node == NULL || node->n >= number)
	{
		max->next = node;
		*head = max;
		return (max);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	max->next = node->next;
	node->next = max;

	return (max);
}
