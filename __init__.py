from aqt import gui_hooks, mw
from aqt.addcards import AddCards


def init(add_cards):
    editor = add_cards.editor
    note = editor.note
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
    
gui_hooks.add_cards_did_init.append(init)
