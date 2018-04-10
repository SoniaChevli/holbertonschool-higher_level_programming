#include "lists.h"
/**
 * insert_node - insert node into sorted linked list
 *@head: start of linked list
 *@number: number to be inserted
 *
 *Return: newlist. otherwise null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *before;
	listint_t *newnode;

	newnode = malloc(sizeof(listint_t));

	if (newnode == NULL)
		return (NULL);

	newnode->n = number;

	if (*head == NULL)
	{
		*head = newnode;
		newnode->next = NULL;
		return (newnode);
	}

	before = *head;

	while (before->next != NULL)
	{
		if (before->next->n > number)
		{
			newnode->next = before->next;
			before->next = newnode;
			return (newnode);
		}
		before = before->next;
	}

	newnode->next = NULL;
	before->next = newnode;

	return (newnode);
}
