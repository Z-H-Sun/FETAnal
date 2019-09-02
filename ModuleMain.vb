Module Module1

    Sub Main()

        Environment.CurrentDirectory = AppDomain.CurrentDomain.BaseDirectory
        Console.Title = "Presettings for FETAnal v1.04 ..."

        Dim P As New Process
        Dim Str As String = "FETAnal.py"
        For Each i In Environment.GetCommandLineArgs.Skip(1)
            If i.ToLower() = "-config" Then : Str += " " & i
            Else : Str += " """ & i & """"
            End If
        Next
        P.StartInfo.FileName = "python.exe"
        P.StartInfo.Arguments = Str
        P.StartInfo.UseShellExecute = False
        P.StartInfo.RedirectStandardError = True

        Try
            P.Start()
        Catch ex As Exception
            Console.ForegroundColor = ConsoleColor.Red
            Console.Write("Python not installed." & vbCrLf)
            Console.ResetColor()
            Console.Write("Press any key to continue ...")
            Console.ReadKey()
            End
        End Try

        Dim ErrMsg As String = P.StandardError.ReadToEnd
        P.WaitForExit()

        If ErrMsg <> "" Then
            If ErrMsg.Contains("No module named") Then
                Dim MM As String
                If ErrMsg.Contains("matplotlib") Then : MM = "matplotlib"
                ElseIf ErrMsg.Contains("numpy") Then : MM = "numpy"
                ElseIf ErrMsg.Contains("xlrd") Then : MM = "xlrd"
                Else
                    Console.ForegroundColor = ConsoleColor.Red
                    Console.Write("Core script error:" & vbCrLf & ErrMsg)
                    Console.ResetColor()
                    Console.Write(vbCrLf & "Press any key to continue ... ")
                    Console.ReadKey()
                    End
                End If

                If MM <> vbNullString Then
                    Console.ForegroundColor = ConsoleColor.Red
                    Console.Write("Module " & MM & " not found." & vbCrLf)
                    Console.ResetColor()
                    Console.Write("Press Y to install, or other keys to continue ... ")

                    If Char.ToLower(Console.ReadKey().KeyChar) = "y" Then
                        Console.Write(vbCrLf & vbCrLf)
                        P.StartInfo.FileName = "pip.exe"
                        P.StartInfo.Arguments = "install " & MM
                        P.StartInfo.UseShellExecute = False
                        P.StartInfo.RedirectStandardError = True
                        Try
                            P.Start()
                        Catch ex As Exception
                            Console.ForegroundColor = ConsoleColor.Red
                            Console.Write("Pip not installed." & vbCrLf)
                            Console.ResetColor()
                            Console.Write("Press any key to continue ...")
                            Console.ReadKey()
                            End
                        End Try

                        ErrMsg = P.StandardError.ReadToEnd
                        P.WaitForExit()
                        If ErrMsg = "" Then
                            Console.ForegroundColor = ConsoleColor.Green
                            Console.Write(vbCrLf & "Installed module " & MM & " successfully")
                            Console.ResetColor()
                            Console.Write(vbCrLf & "Press any key to continue ... ")
                            Console.ReadKey()
                        Else
                            Console.ForegroundColor = ConsoleColor.Yellow
                            Console.Write(vbCrLf & "While installing module " & MM & ", the following error message occurred :" & vbCrLf & ErrMsg)
                            Console.ResetColor()
                            Console.Write(vbCrLf & "Press any key to continue ... ")
                            Console.ReadKey()
                        End If
                    Else
                        End
                    End If

                    Console.Clear()
                    Console.ResetColor()
                    Main()
                End If
            Else
                Console.ForegroundColor = ConsoleColor.Red
                Console.Write("Core script error:" & vbCrLf & ErrMsg)
                Console.ResetColor()
                Console.Write(vbCrLf & "Press any key to continue ... ")
                Console.ReadKey()
            End If
        End If
    End Sub
End Module
