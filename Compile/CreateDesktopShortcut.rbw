require 'win32ole'
WshShell = WIN32OLE.new('WScript.Shell')
strDesktop = WshShell.SpecialFolders('Desktop') # desktop folder

pwd = $Exerb ? ExerbRuntime.filepath : __FILE__.gsub('/', "\\")
pwd = pwd[0, pwd.rindex("\\")] # .exe directory
Dir.chdir(pwd)
targets = [Dir.glob('*/nicsa.exe')[0], Dir.glob('*/FETAnal.exe')[0]] # find target exe's
details = [['\NICS Automator.lnk', '\nicsa.exe', 'Automatic creation of Gaussian input files eligible for NICS(0/1) calculations'] ,['\FET Analyzer.lnk', '\FETAnal.exe', 'Automatic analysis of FET transfer transfer characteristics']]
for i in 0..1
  next if targets[i].nil?
  folder = pwd + "\\" + File.dirname(targets[i])
  oShellLink = WshShell.CreateShortcut(strDesktop + details[i][0])
  oShellLink.TargetPath = folder + details[i][1]
  oShellLink.WorkingDirectory = folder
  oShellLink.Description = details[i][2]
  oShellLink.Save
  f = open(strDesktop + details[i][0], 'r+b')
  begin
    loop do # Find signature A0 00 00 09 [for extra data section]
      if f.readbyte == 9 then
        if f.read(3).bytes == [0, 0, 0xA0] then
          break
        else
          f.seek(-3, IO::SEEK_CUR) # continue finding if the last three bytes does not match 00 00 A0
        end
      end
    end
    f.seek(-8, IO::SEEK_CUR)
  rescue EOFError # if no such signature is found then start writing at EOF
    f.seek(-4, IO::SEEK_END)
  end
  # console properties: cursor/window size; window pos; fore-/background color; font; etc. [https://msdn.microsoft.com/en-us/library/dd891381.aspx]
  f.print "\xCC\0\0\0\2\0\0\xA0\xF0\0\x84\0#{i.zero? ? 'Z':'s'}\0\x88\x13#{i.zero? ? "Z\0\31":"s\0\17"}\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\x14\0006\0\0\0\x90\1\0\0C\0o\0n\0s\0o\0l\0a\0s\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0d\0\0\0\0\0\0\0\1\0\0\0\1\0\0\0\0\0\0\0002\0\0\0\4\0\0\0\0\0\0\0\0\0\0\0\0\0\x80\0\0\x80\0\0\0\x80\x80\0\x80\0\0\0\x80\0\x80\0\x80\x80\0\0\xC0\xC0\xC0\0\x80\x80\x80\0\0\0\xFF\0\0\xFF\0\0\0\xFF\xFF\0\xFF\0\0\0\xFF\0\xFF\0\xFF\xFF\0\0\xFF\xFF\xFF\0\f\0\0\0\4\0\0\xA0\xE9\xFD\0\0"
  f.close
end