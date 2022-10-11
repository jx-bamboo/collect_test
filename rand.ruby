class Ran

	def pwd
		num = ARGV[0].to_i
		puts "begin"
		chars = ("a".."z").to_a + ("0".."9").to_a + ("A".."Z").to_a
		password = ""
		1.upto(num){password << chars[rand(chars.length-1)]}
		puts chars.length
		puts "********************Your PassWord is :" + password + "********************"
		puts "end"
		puts "\a"
	end
 
	

end

t = Ran.new
t.pwd

