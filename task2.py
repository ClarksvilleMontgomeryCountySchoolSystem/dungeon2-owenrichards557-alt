good = r"""      \   / /V\   r _  / \
       \O/  \O/  /O/   \O/
        #    #    #     #
       / \  / \  / \   / \
      ^   ^^   ^^   ^ ^   ^"""
bad = r"""              .__
             //  `-.|/
           () \_  .  \ "Ahh.. Ahh... Ahh..."
           (_()~/\  '|
           /\\  _/  //
  /)))     \_    |  /
 /  |/)   ___)   \/__
 \___/   / \ \  / /  \
  \   \ /   \/\/\/    \
   \   /     \../      \
    \      |_ \/   |   |
     \    /|  o    |   |
      \__/ |  o    |   |  JRO"""
has_key = True

if has_key:
    outcome = "Click: Please put it out your scaring me"
    print(good)
else:
    outcome = "Doom: Please light it again i want it"
    print(bad)
print(outcome)