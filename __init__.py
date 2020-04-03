from aqt import gui_hooks
from aqt.addcards import AddCards


old_init = AddCards.__init__
def init(add_cards, mw):
    old_init(add_cards, mw)
    editor = add_cards.editor
    note = editor.note
    if not isinstance(add_cards, AddCards):
        return
    if note is None:
        return
    if mw.state != "review":
        return
    reviewer = mw.reviewer
    current_card = reviewer.card
    if current_card is None:
        return
    current_note = current_card.note()
    editor.note.setTagsFromStr(current_note.stringTags())
    editor.updateTags()
    current_did = current_card.odid or current_card.did
    current_deck = mw.col.decks.get(current_did)
    add_cards.deckChooser.setDeckName(current_deck["name"])
    
# For .24:
# gui_hooks.add_cards_did_init.append(init)

AddCards.__init__ = init
