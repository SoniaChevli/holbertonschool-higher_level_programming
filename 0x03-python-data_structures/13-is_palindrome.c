#include "lists.h"
/**
 * check_palindrome - checks array to see if palindrome
 * @arr: array of integers
 * @length: length of palindrome
 *
 * Return: 1 if palindrome. 0 if not palindrome.
 */
int check_palindrome(int *arr, int length)
{
	unsigned int beginning = 0;

	while (arr[beginning] <= arr[length])
	{
		if (arr[beginning] != arr[length])
			return (0);
		beginning++;
		length--;
	}
	return (1);

}
/**
 * palindrome_length - finds length of palindrome
 * @head: pointer to linked list
 *
 * Return: length
 */
int palindrome_length(listint_t *head)
{
	int length = 0;

	while (head != NULL)
	{
		head = head->next;
		length++;
	}
	return (length);
}


/**
 * is_palindrome - checks a singly linked list to see if palindrome
 * @head: points to head of list
 *
 * Return: 1 if palindrome. Otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp;
	int *list_arr;
	unsigned int length = 0;
	unsigned int i = 0;

	tmp = *head;
	if (*head == NULL)
		return (1);

	length = palindrome_length(*head);

	if (length == 0)
		return (1);

	list_arr = malloc(sizeof(int) * length);
	if (list_arr == NULL)
		return (0);

	while (tmp != NULL)
	{
		list_arr[i] = tmp->n;
		tmp = tmp->next;
		length++;
	}

	if (check_palindrome(list_arr, length) == 0)
		return (0);
	return (1);

}
