# Copy current deck/tags in add card
## Rationale
You may want to add a note related to the current card, and so have it in
the same deck and with the same tags as the current card. This is
especially useful if you use filtered decks or nested decks. This
add-on simply ensures that, when you are reviewing a card and open
the "add-card" window, its deck will be the deck of the card you are
reviewing, and it will copy its tags.

This was commissioned for 20$.

## Internal
It changes `AddCards.__init__`, and call the previous method. In anki
2.1.24 hopefully it'll use a hook.

## Links, licence and credits

Key         |Value
------------|-------------------------------------------------------------------
Copyright   | Arthur Milchior <arthur@milchior.fr>,
            | p4nix
Based on    | Anki code by Damien Elmes <anki@ichi2.net>
License     | GNU GPL, version 3 or later; http://www.gnu.org/licenses/gpl.html
Source in   | https://github.com/Arthur-Milchior/anki-copy-currentcard-in-add-card
Addon number| [676957592](https://ankiweb.net/shared/info/676957592)
