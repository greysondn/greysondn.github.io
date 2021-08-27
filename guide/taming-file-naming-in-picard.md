---
layout: page
title: Taming File Naming in Picard
permalink: /guide/taming-file-naming-in-picard
---

Mostly this is just where I'm stashing my notes for how to do this so I don't forget, because I'm pretty absent minded, but other people may find it useful.

Process
=======
Scan in Picard (no big deal) then check...

* if the genre is soundtrack
  * set Album Artist, Album Artist Sort Order, and Genre...
    * Movie? "Movie Soundtrack"
    * TV? "TV Soundtrack"
    * Cartoon? "Cartoon Soundtrack"
    * Anime? "Anime Soundtrack"
    * Video Game? "Video Game Soundtrack?"
    * All others? "Soundtrack" or expand this list.

File Rename script
==================

{% highlight text %}
$noop(
    ----------------------------------------------------------------------------
    Make sure we're not a soundtrack. If we are, fix the album artist tag.
    ----------------------------------------------------------------------------
    Pythonic version:
        if genre.contains["Soundtrack"]:
            albumartist = "Soundtrack"
        if genre.contains["Movie Soundtrack"]:
            albumartist = "Movie Soundtrack"
)
$if($in(%genre%, Soundtrack), $set(%albumartist%, Soundtrack))
$if($in(%genre%, Movie Soundtrack), $set(%albumartist%, Movie Soundtrack))

$noop(
    ----------------------------------------------------------------------------
    First folder, should be album artist, unless it's a soundtrack of some sort
    ----------------------------------------------------------------------------
    Pythonic version:
        ret = ""
        
        if albumArtist != None:
            ret = ret + albumArtist
        else:
            ret = ret + "Unknown Artist"
        
        ret = ret + "/"
        
        return ret
)

$if2(%albumartist%, Unknown Artist)/


$noop(
    ----------------------------------------------------------------------------
    Second folder, should be album.
    ----------------------------------------------------------------------------
    Pythonic version:
        ret = ""
        
        if album != None:
            ret = ret + album
        else:
            ret = ret + "Unknown Album"
        
        ret = ret + "/"
        
        return ret
)

$if2(%album%, Unknown Album)/

$noop(
    ----------------------------------------------------------------------------
    Third folder, optional, would be disc number if more than one disc.
    ----------------------------------------------------------------------------
    Pythonic version:
        ret = ""
        
        if totaldiscs > 1:
            # all these squares should be normal parens
            ret = "Disc " str[discnumber].zfill[len[str[totaldiscs]]] + "/"
        
        return ret
)
$if($gt(%totaldiscs%,1),Disc $num(%discnumber%,$len(%totaldiscs%)))/


$noop(
    ----------------------------------------------------------------------------
    Last object, should be track
    ----------------------------------------------------------------------------
    
    Pythonic version:
        ret = ""
        
        # all these squares should be normal parens
        ret = str[tracknumber].zfill[len[str[totaltracks]]] + " " + title
        
        return ret
)

$num(%tracknumber%,$len(%totaltracks%)) %title%
{% endhighlight %}

