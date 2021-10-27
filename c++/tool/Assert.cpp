#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>
#include <string.h>
#include <cassert> // assert가 정의된 헤더 파일

using namespace std;

void copy(char *dest, char *src)
{
    assert("dest는 NULL이 아니어야함", dest != NULL); // dest이 NULL이면 프로그램 중단
    assert("src는 NULL이 아니어야함" && src != NULL); // src가 NULL이면 프로그램 중단

    strcpy(dest, src); // 문자열 복사
}

int main()
{
    char s1[100];
    char *s2 = "Hello, world!";

    copy(s1, s2); // 정상 동작

    copy(NULL, s2); // NULL이 들어갔으므로 프로그램 중단
    copy(s1, NULL); // NULL이 들어갔으므로 프로그램 중단

    return 0;
}