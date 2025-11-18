---
title: JSONPath functionality
source: https://www.zabbix.com/documentation/current/en/manual/config/items/preprocessing/jsonpath_functionality
downloaded: 2025-11-14 10:34:48
---

# 4 JSONPath functionality

#### Overview

This section outlines the supported JSONPath functionality within item value preprocessing steps.

JSONPath is composed of segments separated by dots. A segment can take the form of a simple word, representing a JSON value name, the wildcard character (`*`), or a more intricate construct enclosed within square brackets. The dot before a bracketed segment is optional and can be omitted.

`$.object.name` | Return `object.name` contents.  
---|---  
`$.object['name']` | Return `object.name` contents.  
`$.object.['name']` | Return `object.name` contents.  
`$["object"]['name']` | Return `object.name` contents.  
`$.['object'].["name"]` | Return `object.name` contents.  
`$.object.history.length()` | Return the number of `object.history` array elements.  
`$[?(@.name == 'Object')].price.first()` | Return the value of the `price` property from the first object named "Object".  
`$[?(@.name == 'Object')].history.first().length()` | Return the number of history array elements from the first object named "Object".  
`$[?(@.price > 10)].length()` | Return the number of objects with a price greater than 10.  
  
See also: [Escaping special characters from LLD macro values in JSONPath](/documentation/current/en/manual/config/items/preprocessing/jsonpath_functionality/escaping_lld_macros).

#### Supported segments

`<name>` | Match object property by name.  
---|---  
`*` | Match all object properties.  
`['<name>']` | Match object property by name.  
`['<name>', '<name>', ...]` | Match object property by any of the listed names.  
`[<index>]` | Match array element by index.  
`[<number>, <number>, ...]` | Match array element by any of the listed indexes.  
`[*]` | Match all object properties or array elements.  
`[<start>:<end>]` | Match array elements by the defined range:  
**< start>** \- the first index to match (including); if not specified, matches all array elements from the beginning; if negative, specifies starting offset from the end of array;  
**< end>** \- the last index to match (excluding); if not specified, matches all array elements to the end; if negative, specifies starting offset from the end of array.  
`[?(<expression>)]` | Match objects/array elements by applying a filter expression.  
  
To find a matching segment ignoring its ancestry (detached segment), it must be prefixed with two dots (`..`). For example, `$..name` or `$..['name']` return values of all `name` properties.

Matched element names can be extracted by adding a tilde (`~`) suffix to the JSONPath. It returns the name of the matched object or an index in string format of the matched array item. The output format follows the same rules as other JSONPath queries - definite path results are returned 'as is', and indefinite path results are returned in an array. However, there is minimal value in extracting the name of an element that matches a definitive path, as it is already known.

#### Filter expression

The filter expression is an arithmetical expression in infix notation.

Supported operands:

`"<text>"`  
`'<text>'` | Text constant.  
  
Example:  
`'value: \\'1\\''`  
`"value: '1'"`  
---|---  
`<number>` | Numeric constant supporting scientific notation.  
  
Example: `123`  
`<jsonpath starting with $>` | Value referred to by the JSONPath from the input document root node; only definite paths are supported.  
  
Example: `$.object.name`  
`<jsonpath starting with @>` | Value referred to by the JSONPath from the current object/element; only definite paths are supported.  
  
Example: `@.name`  
  
Supported operators:

`-` | Binary | Subtraction | Number  
---|---|---|---  
`+` | Binary | Addition | Number  
`/` | Binary | Division | Number  
`*` | Binary | Multiplication | Number  
`==` | Binary | Equality | Boolean (1/0)  
`!=` | Binary | Inequality | Boolean (1/0)  
`<` | Binary | Less than | Boolean (1/0)  
`<=` | Binary | Less than or equal to | Boolean (1/0)  
`>` | Binary | Greater than | Boolean (1/0)  
`>=` | Binary | Greater than or equal to | Boolean (1/0)  
`=~` | Binary | Matches regular expression | Boolean (1/0)  
`!` | Unary | Boolean NOT | Boolean (1/0)  
`||` | Binary | Boolean OR | Boolean (1/0)  
`&&` | Binary | Boolean AND | Boolean (1/0)  
  
#### Functions

Functions can be used at the end of JSONPath. Multiple functions can be chained if the preceding function returns value that is accepted by the following function.

Supported functions:

`avg` | Average value of numbers in an input array | Array of numbers | Number  
---|---|---|---  
`min` | Minimum value of numbers in an input array | Array of numbers | Number  
`max` | Maximum value of numbers in an input array | Array of numbers | Number  
`sum` | Sum of numbers in an input array | Array of numbers | Number  
`length` | Number of elements in an input array | Array | Number  
`first` | The first element of an array | Array | A JSON construct (object, array, value) depending on the contents of the input array  
  
JSONPath aggregate functions accept quoted numeric values. These values are automatically converted from strings to numeric types when aggregation is needed. Incompatible input will cause the function to generate an error.

#### Output value

JSONPaths can be divided into definite and indefinite paths. A definite path can return only null or a single match. An indefinite path can return multiple matches: JSONPaths with detached, multiple name/index lists, array slices, or expression segments. However, when a function is used, the JSONPath becomes definite, as functions always output a single value.

A definite path returns the object/array/value it is referencing. In contrast, an indefinite path returns an array of the matched objects/arrays/values.

The property order in JSONPath query results may not align with the original JSON property order due to internal optimization methods. For example, the JSONPath `$.books[1]["author", "title"]` may return `["title", "author"]`. If preserving the original property order is essential, alternative post-query processing methods should be considered.

#### Path formatting rules

Whitespaces (space, tab character) can be used in bracket notation segments and expressions, for example: `$[ 'a' ][ 0 ][ ?( $.b == 'c' ) ][ : -1 ].first( )`.

Strings should be enclosed with single (`'`) or double (`"`) quotes. Inside the strings, single or double quotes (depending on which are used to enclose it) and backslashes (`\`) are escaped with the backslash (`\`) character.

#### Example
    
    
    {
             "books": [
               {
                 "category": "reference",
                 "author": "Nigel Rees",
                 "title": "Sayings of the Century",
                 "price": 8.95,
                 "id": 1
               },
               {
                 "category": "fiction",
                 "author": "Evelyn Waugh",
                 "title": "Sword of Honour",
                 "price": 12.99,
                 "id": 2
               },
               {
                 "category": "fiction",
                 "author": "Herman Melville",
                 "title": "Moby Dick",
                 "isbn": "0-553-21311-3",
                 "price": 8.99,
                 "id": 3
               },
               {
                 "category": "fiction",
                 "author": "J. R. R. Tolkien",
                 "title": "The Lord of the Rings",
                 "isbn": "0-395-19395-8",
                 "price": 22.99,
                 "id": 4
               }
             ],
             "services": {
               "delivery": {
                 "servicegroup": 1000,
                 "description": "Next day delivery in local town",
                 "active": true,
                 "price": 5
               },
               "bookbinding": {
                 "servicegroup": 1001,
                 "description": "Printing and assembling book in A5 format",
                 "active": true,
                 "price": 154.99
               },
               "restoration": {
                 "servicegroup": 1002,
                 "description": "Various restoration methods",
                 "active": false,
                 "methods": [
                   {
                     "description": "Chemical cleaning",
                     "price": 46
                   },
                   {
                     "description": "Pressing pages damaged by moisture",
                     "price": 24.5
                   },
                   {
                     "description": "Rebinding torn book",
                     "price": 99.49
                   }
                 ]
               }
             },
             "filters": {
               "price": 10,
               "category": "fiction",
               "no filters": "no \"filters\""
             },
             "closed message": "Store is closed",
             "tags": [
               "a",
               "b",
               "c",
               "d",
               "e"
             ]
           }

Copy

✔ Copied

`$.filters.price` | definite | 10  
---|---|---  
`$.filters.category` | definite | fiction  
`$.filters['no filters']` | definite | no "filters"  
`$.filters` | definite | {  
"price": 10,  
"category": "fiction",  
"no filters": "no \"filters\""  
}  
`$.books[1].title` | definite | Sword of Honour  
`$.books[-1].author` | definite | J. R. R. Tolkien  
`$.books.length()` | definite | 4  
`$.tags[:]` | indefinite | ["a", "b", "c", "d", "e" ]  
`$.tags[2:]` | indefinite | ["c", "d", "e" ]  
`$.tags[:3]` | indefinite | ["a", "b", "c"]  
`$.tags[1:4]` | indefinite | ["b", "c", "d"]  
`$.tags[-2:]` | indefinite | ["d", "e"]  
`$.tags[:-3]` | indefinite | ["a", "b"]  
`$.tags[:-3].length()` | definite | 2  
`$.books[0, 2].title` | indefinite | ["Moby Dick", "Sayings of the Century"]  
`$.books[1]['author', "title"]` | indefinite | ["Sword of Honour", "Evelyn Waugh"]  
`$..id` | indefinite | [1, 2, 3, 4]  
`$.services..price` | indefinite | [154.99, 5, 46, 24.5, 99.49]  
`$.books[?(@.id == 4 - 0.4 * 5)].title` | indefinite | ["Sword of Honour"]  
  
Note: This query shows that arithmetical operations can be used in queries; it can be simplified to `$.books[?(@.id == 2)].title`  
`$.books[?(@.id == 2 \|\| @.id == 4)].title` | indefinite | ["Sword of Honour", "The Lord of the Rings"]  
`$.books[?(!(@.id == 2))].title` | indefinite | ["Sayings of the Century", "Moby Dick", "The Lord of the Rings"]  
`$.books[?(@.id != 2)].title` | indefinite | ["Sayings of the Century", "Moby Dick", "The Lord of the Rings"]  
`$.books[?(@.title =~ " of ")].title` | indefinite | ["Sayings of the Century", "Sword of Honour", "The Lord of the Rings"]  
`$.books[?(@.price > 12.99)].title` | indefinite | ["The Lord of the Rings"]  
`$.books[?(@.author > "Herman Melville")].title` | indefinite | ["Sayings of the Century", "The Lord of the Rings"]  
`$.books[?(@.price > $.filters.price)].title` | indefinite | ["Sword of Honour", "The Lord of the Rings"]  
`$.books[?(@.category == $.filters.category)].title` | indefinite | ["Sword of Honour","Moby Dick","The Lord of the Rings"]  
`$.books[?(@.category == "fiction" && @.price < 10)].title` | indefinite | ["Moby Dick"]  
`$..[?(@.id)]` | indefinite | [  
{  
"price": 8.95,  
"id": 1,  
"category": "reference",  
"author": "Nigel Rees",  
"title": "Sayings of the Century"  
},  
{  
"price": 12.99,  
"id": 2,  
"category": "fiction",  
"author": "Evelyn Waugh",  
"title": "Sword of Honour"  
},  
{  
"price": 8.99,  
"id": 3,  
"category": "fiction",  
"author": "Herman Melville",  
"title": "Moby Dick",  
"isbn": "0-553-21311-3"  
},  
{  
"price": 22.99,  
"id": 4,  
"category": "fiction",  
"author": "J. R. R. Tolkien",  
"title": "The Lord of the Rings",  
"isbn": "0-395-19395-8"  
}  
]  
`$.services..[?(@.price > 50)].description` | indefinite | ["Printing and assembling book in A5 format", "Rebinding torn book"]  
`$..id.length()` | definite | 4  
`$.books[?(@.id == 2)].title.first()` | definite | Sword of Honour  
`$..tags.first().length()` | definite | 5  
  
Note: `$..tags` is an indefinite path, so it returns an array of matched elements, i.e., `[["a", "b", "c", "d", "e" ]]`; `first()` returns the first element, i.e., `["a", "b", "c", "d", "e"]`; `length()` calculates the length of the element, i.e.,`5`.  
`$.books[*].price.min()` | definite | 8.95  
`$..price.max()` | definite | 154.99  
`$.books[?(@.category == "fiction")].price.avg()` | definite | 14.99  
`$.books[?(@.category == $.filters.xyz)].title` | indefinite | Note: A query without match returns NULL for definite and indefinite paths.  
`$.services[?(@.active=="true")].servicegroup` | indefinite | [1001,1000]  
  
Note: Text constants must be used in boolean value comparisons.  
`$.services[?(@.active=="false")].servicegroup` | indefinite | [1002]  
  
Note: Text constants must be used in boolean value comparisons.  
`$.services[?(@.servicegroup=="1002")]~.first()` | definite | restoration