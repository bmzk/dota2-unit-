import json
def dump_(str):
    '''写入json文件'''
    file_w=open('f.json','w+',encoding='utf-8')
    
    json.dump(str,file_w,indent=5)
    file_w.close()
'''
['AcceleratorTable', 'AcceptsFocus', 'AcceptsFocusFromKeyboard', 
'AcceptsFocusRecursively', 'AddChild', 'AddFilter', 'AddPendingEvent',
 'AdjustForLayoutDirection', 'AlwaysShowScrollbars', 'AssociateHandle', 
 'AutoLayout', 'BackgroundColour', 'BackgroundStyle', 'BeginRepositioningChildren',
  'BestSize', 'BestVirtualSize', 'Bind', 'Border', 'CacheBestSize', 'CanAcceptFocus',
   'CanAcceptFocusFromKeyboard', 'CanScroll', 'CanSetTransparent', 'CaptureMouse', 
   'Caret', 'Center', 'CenterOnParent', 'Centre', 'CentreOnParent', 'CharHeight', 
   'CharWidth', 'Children', 'ChildrenRepositioningGuard', 'ClassInfo', 'ClassName', 
   'ClearBackground', 'ClientAreaOrigin', 'ClientRect', 'ClientSize', 
   'ClientToScreen', 'ClientToWindowSize', 'Close', 'Command', 'Connect', 
   'Constraints', 'ContainingSizer', 'ConvertDialogPointToPixels', 
   'ConvertDialogSizeToPixels', 'ConvertDialogToPixels', 'ConvertPixelsToDialog', 
   'Create', 'Cursor', 'DLG_UNIT', 'DefaultAttributes', 'DeletePendingEvents', 
'Destroy', 'DestroyChildren', 'DestroyLater', 'Disable', 'Disconnect',
 'DissociateHandle', 'DoEnable', 'DoFreeze', 'DoGetBestClientSize', 
 'DoGetBestSize', 'DoGetBorderSize', 'DoGetClientSize', 'DoGetPosition', 'DoGetSize', 
 'DoMoveWindow', 'DoSetClientSize', 'DoSetSize', 'DoSetSizeHints', 'DoSetWindowVariant', 'DoThaw',
'DoUpdateWindowUI', 'DragAcceptFiles', 'DropTarget', 'EffectiveMinSize', 'Ellipsize',
 'Enable', 'Enabled', 'EndRepositioningChildren', 'EscapeMnemonics', 'EventHandler', 
 'EvtHandlerEnabled', 'ExtraStyle', 'FindFocus', 'FindWindow', 'FindWindowById', 'FindWindowByLabel', 'FindWindowByName', 'Fit', 'FitInside', 'Font', 'ForegroundColour', 'Freeze', 'GetAcceleratorTable', 'GetAccessible', 'GetAutoLayout', 'GetBackgroundColour', 'GetBackgroundStyle', 'GetBestHeight', 'GetBestSize', 'GetBestVirtualSize', 'GetBestWidth', 'GetBorder', 'GetCapture', 'GetCaret', 'GetCharHeight', 'GetCharWidth', 'GetChildren',
'GetWindowVariant', 'GrandParent', 'Handle', 
'HandleAsNavigationKey', 'HandleWindowEvent', 'HasCapture', 
'HasExtraStyle', 'HasFlag', 'HasFocus', 'HasMultiplePages', 'HasScrollbar', 
'HasTransparentBackground', 'HelpText', 'Hide', 'HideWithEffect', 'HitTest', 
'Id', 'InformFirstDirection', 'InheritAttributes', 'InheritsBackgroundColour',
'InitDialog', 'InvalidateBestSize', 'IsBeingDeleted', 'IsDescendant', 'IsDoubleBuffered', 'IsEllipsized', 'IsEnabled', 'IsExposed', 'IsFocusable', 'IsFrozen', 'IsRetained', 'IsSameAs', 'IsScrollbarAlwaysShown', 'IsShown', 'IsShownOnScreen', 'IsThisEnabled', 'IsTopLevel', 'IsTransparentBackgroundSupported', 'IsUnlinked', 'Label', 'LabelText', 'Layout', 'LayoutDirection', 'LineDown', 'LineUp', 'Lower', 'MacIsWindowScrollbar', 'MaxClientSize', 'MaxHeight', 'MaxSize', 'MaxWidth', 'MinClientSize', 'MinHeight', 'MinSize', 'MinWidth', 'Move', 'MoveAfterInTabOrder', 'MoveBeforeInTabOrder', 'MoveXY', 'Name', 'Navigate', 'NavigateIn', 'NewControlId', 'NextHandler', 'OnInternalIdle', 'PageDown', 'PageUp', 'Parent', 'PopEventHandler', 'PopupMenu', 'Position', 'PostCreate', 'PostSizeEvent', 'PostSizeEventToParent', 'PreviousHandler', 'ProcessEvent', 'ProcessEventLocally', 'ProcessPendingEvents', 'ProcessWindowEvent',
'ProcessWindowEventLocally', 'PushEventHandler', 'QueueEvent', 'Raise', 
'Rect', 'Ref', 'RefData', 'Refresh', 'RefreshRect', 'RegisterHotKey', 'ReleaseMouse', 
'RemoveChild', 'RemoveEventHandler', 'RemoveFilter', 'RemoveMnemonics', 'Reparent', 
'SafelyProcessEvent', 'ScreenPosition', 'ScreenRect', 'ScreenToClient', 'ScrollLines', 'ScrollPages', 'ScrollWindow', 'SendDestroyEvent',
'SendIdleEvents', 'SendSizeEvent', 'SendSizeEventToParent', 'SetAcceleratorTable', 
'SetAccessible', 'SetAutoLayout', 'SetBackgroundColour', 'SetBackgroundStyle', 
'SetCanFocus', 'SetCaret', 'SetClientRect', 'SetClientSize', 'SetConstraints', 
'SetContainingSizer', 'SetCursor', 'SetDimensions', 'SetDoubleBuffered', 
'SetDropTarget', 'SetEventHandler', 'SetEvtHandlerEnabled', 'SetExtraStyle', 
'SetFocus', 'SetFocusFromKbd', 'SetFont', 'SetForegroundColour',
'SetHelpText', 'SetId', 'SetInitialSize', 
'SetLabel', 'SetLabelMarkup', 'SetLabelText', 
'SetLayoutDirection', 'SetMaxClientSize', 'SetMaxSize', 
'SetMinClientSize', 'SetMinSize', 'SetName', 'SetNextHandler', 
'SetOwnBackgroundColour', 'SetOwnFont', 'SetOwnForegroundColour', 
'SetPalette', 'SetPosition', 'SetPreviousHandler', 'SetRect', 'SetRefData', 
'SetScrollPos', 'SetScrollbar', 'SetSize', 'SetSizeHints', 'SetSizeHintsSz', 
'SetSizeWH', 'SetSizer', 'SetSizerAndFit', 'SetThemeEnabled', 'SetToolTip', 
'SetToolTipString', 'SetTransparent', 'SetValidator', 'SetVirtualSize', 
'SetVirtualSizeWH', 'SetWindowStyle', 'SetWindowStyleFlag', 'SetWindowVariant', 
'ShouldInheritColours', 'Show', 'ShowWithEffect', 'Shown', 'Size', 'Sizer', 'Thaw', 
'ThemeEnabled', 'ToggleWindowStyle', 'ToolTip', 'TopLevel', 'TopLevelParent', 
'TransferDataFromWindow', 'TransferDataToWindow', 'TryAfter', 'TryBefore', 
'UnRef', 'UnShare', 'Unbind', 'Unlink', 'UnregisterHotKey', 'UnreserveControlId', 
'UnsetToolTip', 'Update', 'UpdateClientRect', 'UpdateRegion', 'UpdateWindowUI', 
'UseBgCol', 'Validate', 'Validator', 'VirtualSize', 'WarpPointer', 'WindowStyle', 
'WindowStyleFlag', 'WindowToClientSize', 'WindowVariant', 'Wrap', '''
