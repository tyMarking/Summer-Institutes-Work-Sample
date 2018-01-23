/**
 * Implements a dictionary's functionality.
 */

#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

#include "dictionary.h"
node firstNode;
unloadNode *firstUnloadNode;
unloadNode *currentUnloadNode;
/**
 * Returns true if word is in dictionary else false.
 */
char *wordCopy;
bool check(const char *word)
{
    memset(wordCopy, 0, (LENGTH+2)*sizeof(char));
    for (int i = 0; i<strlen(word); i++) {
        *(wordCopy+(i*sizeof(char))) = tolower(*(word+(i*sizeof(char))));
    }
    return checkRec(wordCopy, &firstNode);
}
int location = 0;
bool checkRec(char *word, node *pNode) {
    if (word == NULL || strlen(word) == 0) {
        if (pNode -> isEOW == true) {
            return true;
        } else {
            return false;
        }
    }
    if ( *word == 39) {
        location = 26; 
    } else {
        location = (*word)-97;
    }
    if (pNode -> children[location] == NULL) {
        return false;
    } else {
        return checkRec(word+1, pNode -> children[location]);
    }
}

//for size function
int sizeOfDict = 0;

/**
 * Loads dictionary into memory. Returns true if successful else false.
 */
FILE *dict;
char *in;
int childrenPointerSize;
bool load(const char *dictionary)
{
    wordCopy = malloc((LENGTH+2)*sizeof(char));
    if (dictionary == NULL) {
        return false;
    }
    dict = fopen(dictionary, "r");
    if (dict == NULL) {
        return false;
    }
    firstNode.isEOW = false;
    firstNode.character = false;
    firstUnloadNode = malloc(sizeof(unloadNode));
    firstUnloadNode -> node = NULL;
    //firstUnloadNode -> unloadNode = NULL;
    currentUnloadNode = firstUnloadNode;
    for (int i = 0; i<27; i++) {
            firstNode.children[i] = NULL;
    }
    in = malloc((LENGTH+2)*sizeof(char));
    sizeOfDict = 0;
    childrenPointerSize = sizeof(node *) * 27;
    while (fgets(in, LENGTH+2, dict) != NULL) {
        sizeOfDict ++;
        createNodes(in, &firstNode);
    }
    return true;
}

/**
 * Recursive method for creating nodes to represent chars of word
 */
node *newNode;
unloadNode *newUnloadNode;
void createNodes(char *word, node *pNode) {
    if ((*word) == 39) {
        location = 26; 
    } else {
        location = (*word)-97;
    }
    if (pNode -> children[location] == NULL) {
        newNode = malloc(224);
        newNode -> character = *word;
        newNode -> isEOW = false;
        memset(&(newNode -> children[0]), 0, childrenPointerSize);
        pNode -> children[location] = newNode;
        
        newUnloadNode = malloc(16);
        currentUnloadNode -> unloadNode = newUnloadNode;
        newUnloadNode -> node = newNode;
        newUnloadNode -> unloadNode = NULL;
        currentUnloadNode = newUnloadNode;
    } else {
        newNode = pNode -> children[location];   
    }
    if (*(word+1) == '\n') {
        newNode -> isEOW = true;
        return;
    } else {
        return createNodes(word+sizeof(char), newNode);
    }
}


/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void)
{
    // is 0 by default so if not loaded will be zero
    return sizeOfDict;
}

/**
 * Unloads dictionary from memory. Returns true if successful else false.
 */
bool unload(void)
{
    // TODO
    fclose(dict);
    free(wordCopy);
    free(in);
    /*for (int i = 0; i<27; i++) {
        unloadNodes(firstNode.children[i]);
    }*/
    unloadNode *lastUnloadNode;
    currentUnloadNode = firstUnloadNode;
    //printf("Hi there\n");
    bool null = false;
    while (!null) {
        //printf("oh okay then\n");
        lastUnloadNode = currentUnloadNode;
        if (currentUnloadNode -> unloadNode == NULL) {
            null = true;
        } else {
            currentUnloadNode = currentUnloadNode -> unloadNode;
        }
        free(lastUnloadNode -> node);
        free(lastUnloadNode);
    }
    //printf("Good bye\n");
    //free (firstUnloadNode);
    //free (currentUnloadNode);
    //free (lastUnloadNode);
    return true;
}

void unloadNodes (node *node) {
    if (node == NULL) {
        return;
    }
    for (int i = 0; i<27; i++) {
        if (node -> children[i] != NULL) {
            unloadNodes(node -> children[i]);
        }
    }
    free (node);
    return;
}
