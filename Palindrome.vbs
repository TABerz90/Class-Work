Module Program

    Sub declaration()
        Dim input As String
        Dim index, length As Integer
        Dim pallin As Boolean
    End Sub

    Sub input()
        pallin = True
        Console.Write("Enter the word: ")
        input = Console.ReadLine

        length = Len(input) - 1
    End Sub

    Sub arrays()
        Dim orignal(0 To length) As String
        Dim reverse(0 To length) As String

        For index = 0 To length
            orignal(index) = input.Chars(index)
            reverse(length - index) = input.Chars(index)
        Next
    End Sub

    Sub compare()

        For index = 0 To length
            If orignal(index) <> reverse(index) Then
                pallin = False
            End If
        Next
    End Sub

    Sub output()

        If pallin = False Then
            Console.WriteLine("not a pallin")
        Else
            Console.WriteLine("is a pallin")
        End If
    End Sub
    Sub Main()

        Do
            Call declaration()
            Call input()
            Call arrays()
            Call compare()
            Call output()
        Loop Until pallin = True

    End Sub
End Module
