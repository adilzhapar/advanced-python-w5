# Develop key-value storage ( CLI )
___

## Goal
> Your goal is to develop a key-value storage based on the command line interface (CLI).    
> Data storage should be implemented using files.    
> Examples of commands are below

<br>


### Save variable
```shell
./storage --key key_name --value value
```

### Read variable
```shell
./storage --key key_name
```

### Delete variable

```shell
./storage --key key_name -delete
```


## Example  
```shell
$ ./storage --key mykey --value test
$ ./storage --key mykey
test
$ ./storage --key multi_key --value test1
$ ./storage --key multi_key --value test2
$ ./storage --key multi_key
test1, test2
```
