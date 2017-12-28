call plug#begin('~/.vim/plugged')

Plug 'Valloric/YouCompleteMe'
Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }
Plug 'morhetz/gruvbox'
Plug 'Xuyuanp/nerdtree-git-plugin'
Plug 'nightsense/vim-crunchbang'
Plug 'octol/vim-cpp-enhanced-highlight'
Plug 'tpope/vim-capslock'
Plug 'tpope/vim-surround'
Plug 'tpope/vim-commentary'
Plug 'SirVer/ultisnips', { 'on': [] }
Plug 'honza/vim-snippets'
Plug 'tpope/vim-surround'

call plug#end()
set nocompatible

source $VIMRUNTIME/mswin.vim
behave mswin

syntax on
colorscheme gruvbox
set background=dark

let g:cpp_class_scope_highlight=1
let g:cpp_member_variable_highlight=1

"Numbers
set number
set completeopt-=preview
set backspace=2 "backspace deletes like most programs in insert mode
set showcmd "display incomplete command
set wildmenu
set lazyredraw "redraw only when we need to
set showmatch "highlight matching[{()}]
set autowrite "automatically :write before running commands
set ruler "show the cursor position all the time
set autoread "reload file changed outside vim
set cursorline "highlight the current line
filetype indent on
set visualbell "stop that ANNOYING beeping
set guifont=Mono\ 16

"Make searching better
set gdefault "Never have to type /g at the end of search / replace again

"Softtabs, 2 spaces
set expandtab
set tabstop=4
set softtabstop=4
set shiftwidth=2
set shiftround

" snippets
augroup load_us_ycm
  autocmd!
  autocmd InsertEnter * call plug#load('ultisnips', 'YouCompleteMe')
                     \| autocmd! load_us_ycm
augroup END
" end snippets
let g:UltiSnipsExpandTrigger="<tab>"
let g:UltiSnipsJumpForwardTrigger="<c-b>"
let g:UltiSnipsJumpBackwardTrigger="<c-z>"

"make it obvious where 100 characters is 
set textwidth=100
"set formatoptions=cq
set formatoptions=qrn1
set wrapmargin=0
set colorcolumn=+1

"Auto resize Vim splits to active split
set winwidth=80 
set winheight=5
set winminheight=5
set winheight=999

"Start scrolling when we're 8 lines awawy from margins
set scrolloff=8
"set sidescrolloff=15
"set sidescroll=1

"Use tab to jump between blocks, because it's easier

set hlsearch " highlight matches
set incsearch " search as characters are entered

"building
au FileType cpp set makeprg=g++\ %

nnoremap <C-]> :make!<CR>
nnoremap <C-\> :!.n 'tpope/vim-surround'/a.out<CR>
noremap <F5> :!python3 %<CR>
inoremap <F5> <ESC>:!python3 %<CR>
"remap CapsLock
inoremap kj <Esc>
noremap <Leader>y "*y
noremap <Leader>p "*p
noremap <Leader>Y "+y
noremap <Leader>P "+p
nnoremap <leader><space> :nohlsearch<CR> "turn off search highlight

map <C-n> :NERDTreeToggle<CR>

map <silent> <C-h> :call WinMove('h')<CR>
map <silent> <C-j> :call WinMove('j')<CR>
map <silent> <C-k> :call WinMove('k')<CR>
map <silent> <C-l> :call WinMove('l')<CR>
function! WinMove(key)
        let t:curwin = winnr()
        exec "wincmd ".a:key
        if (t:curwin == winnr())
                if (match(a:key,'[jk]'))
                   wincmd v
                else
                   wincmd s
                endif
                exec "wincmd ".a:key
        endif
endfunction

