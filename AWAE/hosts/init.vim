call plug#begin("~/.vim/plugged")
	Plug 'preservim/nerdtree'
	Plug 'ryanoasis/vim-devicons'
	Plug 'morhetz/gruvbox'
	Plug 'neoclide/coc.nvim', {'branch': 'release'}
	Plug 'vimwiki/vimwiki'
	Plug 'jiangmiao/auto-pairs'
	Plug 'mattn/emmet-vim'
	"Latex plugins
	Plug 'SirVer/ultisnips'
	Plug 'honza/vim-snippets'
	Plug 'lervag/vimtex'
	Plug 'puremourning/vimspector'
	Plug 'tomlion/vim-solidity'
	Plug 'vimwiki/vimwiki'
	Plug 'blackcauldron7/surround.nvim'
"	Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
"	Plug 'roxma/nvim-yarp'
"  	Plug 'roxma/vim-hug-neovim-rpc'
call plug#end()

set nocompatible
filetype plugin indent on
set smartindent
syntax on

lua require"surround".setup{}

colorscheme gruvbox
let g:coc_global_extensions = ['coc-emmet', 'coc-css', 'coc-html', 'coc-json', 'coc-prettier', 'coc-tsserver']
let g:NERDTreeShowHidden = 1
let g:NERDTreeMinimalUI = 1
let g:NERDTreeIgnore = []
let g:NERDTreeStatusline = ''
set encoding=utf8
let g:airline_powerline_fonts = 1
" Automaticaly close nvim if NERDTree is only thing left open
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
" Toggle
nnoremap <silent> <C-b> :NERDTreeToggle<CR>

" Set the filetype based on the file's extension, but only if
" 'filetype' has not already been set
au BufRead,BufNewFile *.handlebars setfiletype html

"Latex config stuff
"let g:deoplete#enable_at_startup = 1

" Trigger configuration. You need to change this to something other than <tab> if you use one of the following:
" - https://github.com/Valloric/YouCompleteMe
" - https://github.com/nvim-lua/completion-nvim
let g:UltiSnipsExpandTrigger="<tab>"
let g:UltiSnipsJumpForwardTrigger="<c-b>"
let g:UltiSnipsJumpBackwardTrigger="<c-z>"

" If you want :UltiSnipsEdit to split your window.
let g:UltiSnipsEditSplit="vertical"

" This is new style
"call deoplete#custom#var('omni', 'input_patterns', {'tex': g:vimtex#re#deoplete})
"
"Config for vimspector
let g:vimspector_enable_mapping = 'HUMAN'
nmap <leader>dd :call vimspector#Launch()<CR>
nmap <leader>dx :VimspectorReset<CR> 
nmap <leader>de :VimspectorEval<CR> 
nmap <leader>dw :VimspectorWatch<CR> 

"Configuration fo Vimwiki
" Vim Wiki
"let g:vimwiki_list = [{'path': '~/Documents', 'syntax': 'markdown'}]
"au FileType vimwiki setlocal shiftwidth=6 tabstop=6 noexpandtab
